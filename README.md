# SyndProxy private pool

## Current pool

- Alive now: 942
- Gold now: 406
- HTTP: 254 alive / 90 gold
- HTTPS: 194 alive / 23 gold
- SOCKS4: 221 alive / 127 gold
- SOCKS5: 273 alive / 166 gold

## Historical pool

- Discovered: 164910
- Ever alive: 32128
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
