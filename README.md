# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 437
- HTTP: 110 alive / 83 gold
- HTTPS: 48 alive / 24 gold
- SOCKS4: 165 alive / 161 gold
- SOCKS5: 197 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44548
- Ever gold: 1405

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
