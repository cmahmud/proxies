# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 334
- HTTP: 117 alive / 35 gold
- HTTPS: 53 alive / 10 gold
- SOCKS4: 171 alive / 148 gold
- SOCKS5: 171 alive / 141 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32790
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
