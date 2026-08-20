# SyndProxy private pool

## Current pool

- Alive now: 1495
- Gold now: 586
- HTTP: 603 alive / 204 gold
- HTTPS: 434 alive / 97 gold
- SOCKS4: 226 alive / 150 gold
- SOCKS5: 232 alive / 135 gold

## Historical pool

- Discovered: 136255
- Ever alive: 22841
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
