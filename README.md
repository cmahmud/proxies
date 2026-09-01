# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 455
- HTTP: 127 alive / 86 gold
- HTTPS: 131 alive / 33 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 190 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46624
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
