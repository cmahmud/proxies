# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 477
- HTTP: 143 alive / 99 gold
- HTTPS: 122 alive / 41 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 199 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45053
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
