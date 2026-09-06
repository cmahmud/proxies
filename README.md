# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 392
- HTTP: 111 alive / 72 gold
- HTTPS: 38 alive / 15 gold
- SOCKS4: 166 alive / 151 gold
- SOCKS5: 187 alive / 154 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48214
- Ever gold: 1525

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
