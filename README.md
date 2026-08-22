# SyndProxy private pool

## Current pool

- Alive now: 897
- Gold now: 403
- HTTP: 262 alive / 79 gold
- HTTPS: 178 alive / 27 gold
- SOCKS4: 214 alive / 155 gold
- SOCKS5: 243 alive / 142 gold

## Historical pool

- Discovered: 165846
- Ever alive: 32376
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
