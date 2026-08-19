# SyndProxy private pool

## Current pool

- Alive now: 1132
- Gold now: 414
- HTTP: 367 alive / 92 gold
- HTTPS: 269 alive / 20 gold
- SOCKS4: 221 alive / 142 gold
- SOCKS5: 275 alive / 160 gold

## Historical pool

- Discovered: 136185
- Ever alive: 22303
- Ever gold: 895

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
