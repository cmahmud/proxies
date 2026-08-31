# SyndProxy validated proxy pool

## Current pool

- Alive now: 670
- Gold now: 481
- HTTP: 158 alive / 104 gold
- HTTPS: 140 alive / 41 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 201 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45234
- Ever gold: 1427

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
