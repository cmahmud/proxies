# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 481
- HTTP: 154 alive / 97 gold
- HTTPS: 124 alive / 48 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 195 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45026
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
