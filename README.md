# SyndProxy private pool

## Current pool

- Alive now: 1041
- Gold now: 419
- HTTP: 312 alive / 93 gold
- HTTPS: 188 alive / 24 gold
- SOCKS4: 258 alive / 144 gold
- SOCKS5: 283 alive / 158 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28154
- Ever gold: 1107

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
