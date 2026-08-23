# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 371
- HTTP: 91 alive / 51 gold
- HTTPS: 40 alive / 11 gold
- SOCKS4: 171 alive / 154 gold
- SOCKS5: 189 alive / 155 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33029
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
