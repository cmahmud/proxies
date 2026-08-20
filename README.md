# SyndProxy private pool

## Current pool

- Alive now: 1400
- Gold now: 582
- HTTP: 547 alive / 203 gold
- HTTPS: 398 alive / 94 gold
- SOCKS4: 226 alive / 150 gold
- SOCKS5: 229 alive / 135 gold

## Historical pool

- Discovered: 136255
- Ever alive: 22841
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
