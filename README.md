# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 389
- HTTP: 88 alive / 47 gold
- HTTPS: 67 alive / 15 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41612
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
