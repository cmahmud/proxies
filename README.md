# SyndProxy validated proxy pool

## Current pool

- Alive now: 665
- Gold now: 470
- HTTP: 163 alive / 95 gold
- HTTPS: 133 alive / 37 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 197 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45186
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
