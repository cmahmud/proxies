# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 481
- HTTP: 145 alive / 96 gold
- HTTPS: 129 alive / 47 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 199 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45021
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
