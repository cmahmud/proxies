# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 475
- HTTP: 171 alive / 103 gold
- HTTPS: 118 alive / 37 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 197 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45209
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
