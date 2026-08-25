# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 427
- HTTP: 96 alive / 67 gold
- HTTPS: 87 alive / 27 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 189 alive / 172 gold

## Historical pool

- Discovered: 183874
- Ever alive: 35706
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
