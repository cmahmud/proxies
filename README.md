# SyndProxy private pool

## Current pool

- Alive now: 1041
- Gold now: 426
- HTTP: 317 alive / 92 gold
- HTTPS: 194 alive / 24 gold
- SOCKS4: 253 alive / 146 gold
- SOCKS5: 277 alive / 164 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28155
- Ever gold: 1107

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
