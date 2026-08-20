# SyndProxy private pool

## Current pool

- Alive now: 879
- Gold now: 407
- HTTP: 226 alive / 83 gold
- HTTPS: 158 alive / 24 gold
- SOCKS4: 225 alive / 145 gold
- SOCKS5: 270 alive / 155 gold

## Historical pool

- Discovered: 151071
- Ever alive: 27445
- Ever gold: 1097

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
