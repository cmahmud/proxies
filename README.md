# SyndProxy validated proxy pool

## Current pool

- Alive now: 657
- Gold now: 469
- HTTP: 157 alive / 93 gold
- HTTPS: 130 alive / 38 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 197 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45186
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
