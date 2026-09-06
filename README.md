# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 389
- HTTP: 105 alive / 71 gold
- HTTPS: 33 alive / 15 gold
- SOCKS4: 168 alive / 150 gold
- SOCKS5: 181 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48232
- Ever gold: 1525

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
