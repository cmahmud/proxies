# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 444
- HTTP: 145 alive / 79 gold
- HTTPS: 92 alive / 32 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 225 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45440
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
