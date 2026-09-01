# SyndProxy validated proxy pool

## Current pool

- Alive now: 650
- Gold now: 454
- HTTP: 118 alive / 88 gold
- HTTPS: 126 alive / 31 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 225 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46548
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
