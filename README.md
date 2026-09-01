# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 459
- HTTP: 129 alive / 91 gold
- HTTPS: 134 alive / 32 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 187 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46677
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
