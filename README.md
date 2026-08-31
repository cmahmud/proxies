# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 443
- HTTP: 119 alive / 78 gold
- HTTPS: 85 alive / 30 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 203 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45455
- Ever gold: 1432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
