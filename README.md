# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 416
- HTTP: 105 alive / 73 gold
- HTTPS: 47 alive / 20 gold
- SOCKS4: 186 alive / 158 gold
- SOCKS5: 183 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49463
- Ever gold: 1584

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
