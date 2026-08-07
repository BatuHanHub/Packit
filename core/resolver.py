def resolvePackages(manager, packageMap):
    packages = []

    for handle in manager["handles"]:
        packages.extend(packageMap.get(handle, []))

    return packages