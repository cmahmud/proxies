# SyndProxy private pool

## Current pool

- Alive now: 793
- Gold now: 373
- HTTP: 214 alive / 67 gold
- HTTPS: 164 alive / 21 gold
- SOCKS4: 211 alive / 147 gold
- SOCKS5: 204 alive / 138 gold

## Historical pool

- Discovered: 148334
- Ever alive: 26176
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
