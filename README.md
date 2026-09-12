# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 472
- HTTP: 137 alive / 100 gold
- HTTPS: 63 alive / 37 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 191 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49365
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
