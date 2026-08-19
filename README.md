# SyndProxy private pool

## Current pool

- Alive now: 1159
- Gold now: 551
- HTTP: 435 alive / 189 gold
- HTTPS: 276 alive / 104 gold
- SOCKS4: 236 alive / 118 gold
- SOCKS5: 212 alive / 140 gold

## Historical pool

- Discovered: 124841
- Ever alive: 19293
- Ever gold: 771

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
