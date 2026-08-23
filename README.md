# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 333
- HTTP: 115 alive / 35 gold
- HTTPS: 55 alive / 10 gold
- SOCKS4: 173 alive / 147 gold
- SOCKS5: 171 alive / 141 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32790
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
