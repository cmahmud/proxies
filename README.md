# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 410
- HTTP: 101 alive / 66 gold
- HTTPS: 80 alive / 20 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 181 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38607
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
