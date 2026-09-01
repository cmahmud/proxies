# SyndProxy validated proxy pool

## Current pool

- Alive now: 639
- Gold now: 446
- HTTP: 123 alive / 84 gold
- HTTPS: 125 alive / 30 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 217 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46605
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
