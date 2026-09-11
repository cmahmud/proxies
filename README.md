# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 424
- HTTP: 91 alive / 68 gold
- HTTPS: 45 alive / 21 gold
- SOCKS4: 188 alive / 164 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48891
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
