# SyndProxy validated proxy pool

## Current pool

- Alive now: 695
- Gold now: 464
- HTTP: 171 alive / 95 gold
- HTTPS: 123 alive / 35 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 229 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45305
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
