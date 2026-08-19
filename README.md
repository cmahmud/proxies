# SyndProxy private pool

## Current pool

- Alive now: 890
- Gold now: 343
- HTTP: 290 alive / 71 gold
- HTTPS: 189 alive / 17 gold
- SOCKS4: 191 alive / 111 gold
- SOCKS5: 220 alive / 144 gold

## Historical pool

- Discovered: 111011
- Ever alive: 16142
- Ever gold: 508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
