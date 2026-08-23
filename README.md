# SyndProxy validated proxy pool

## Current pool

- Alive now: 455
- Gold now: 364
- HTTP: 76 alive / 45 gold
- HTTPS: 33 alive / 9 gold
- SOCKS4: 167 alive / 155 gold
- SOCKS5: 179 alive / 155 gold

## Historical pool

- Discovered: 173623
- Ever alive: 33016
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
