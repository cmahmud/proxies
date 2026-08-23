# SyndProxy validated proxy pool

## Current pool

- Alive now: 463
- Gold now: 361
- HTTP: 79 alive / 42 gold
- HTTPS: 35 alive / 9 gold
- SOCKS4: 168 alive / 155 gold
- SOCKS5: 181 alive / 155 gold

## Historical pool

- Discovered: 173623
- Ever alive: 33016
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
