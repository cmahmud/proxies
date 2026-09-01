# SyndProxy validated proxy pool

## Current pool

- Alive now: 610
- Gold now: 454
- HTTP: 123 alive / 87 gold
- HTTPS: 128 alive / 32 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 186 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46620
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
