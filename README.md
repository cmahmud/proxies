# SyndProxy validated proxy pool

## Current pool

- Alive now: 604
- Gold now: 455
- HTTP: 123 alive / 87 gold
- HTTPS: 124 alive / 32 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 186 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46622
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
