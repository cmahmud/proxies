# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 414
- HTTP: 123 alive / 72 gold
- HTTPS: 148 alive / 21 gold
- SOCKS4: 181 alive / 157 gold
- SOCKS5: 191 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40519
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
