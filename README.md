# SyndProxy validated proxy pool

## Current pool

- Alive now: 661
- Gold now: 462
- HTTP: 127 alive / 91 gold
- HTTPS: 132 alive / 36 gold
- SOCKS4: 181 alive / 160 gold
- SOCKS5: 221 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46502
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
