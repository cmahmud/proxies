# SyndProxy validated proxy pool

## Current pool

- Alive now: 654
- Gold now: 478
- HTTP: 154 alive / 100 gold
- HTTPS: 138 alive / 41 gold
- SOCKS4: 164 alive / 159 gold
- SOCKS5: 198 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45215
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
