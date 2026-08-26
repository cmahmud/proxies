# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 410
- HTTP: 105 alive / 65 gold
- HTTPS: 75 alive / 19 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 181 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38633
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
