# SyndProxy validated proxy pool

## Current pool

- Alive now: 660
- Gold now: 477
- HTTP: 154 alive / 104 gold
- HTTPS: 138 alive / 38 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 197 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45232
- Ever gold: 1427

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
