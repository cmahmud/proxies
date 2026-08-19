# SyndProxy private pool

## Current pool

- Alive now: 1214
- Gold now: 551
- HTTP: 456 alive / 184 gold
- HTTPS: 296 alive / 101 gold
- SOCKS4: 221 alive / 121 gold
- SOCKS5: 241 alive / 145 gold

## Historical pool

- Discovered: 124836
- Ever alive: 19277
- Ever gold: 771

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
