# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 420
- HTTP: 102 alive / 67 gold
- HTTPS: 50 alive / 18 gold
- SOCKS4: 191 alive / 164 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48914
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
