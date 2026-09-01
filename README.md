# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 457
- HTTP: 133 alive / 89 gold
- HTTPS: 135 alive / 32 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 191 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46637
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
