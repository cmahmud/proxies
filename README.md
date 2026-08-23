# SyndProxy validated proxy pool

## Current pool

- Alive now: 462
- Gold now: 362
- HTTP: 79 alive / 44 gold
- HTTPS: 35 alive / 9 gold
- SOCKS4: 168 alive / 155 gold
- SOCKS5: 180 alive / 154 gold

## Historical pool

- Discovered: 173623
- Ever alive: 33016
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
