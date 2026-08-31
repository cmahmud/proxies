# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 446
- HTTP: 144 alive / 77 gold
- HTTPS: 99 alive / 34 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 209 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45391
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
