# SyndProxy validated proxy pool

## Current pool

- Alive now: 655
- Gold now: 479
- HTTP: 155 alive / 101 gold
- HTTPS: 128 alive / 40 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 191 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45248
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
